import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ChandeMomentumOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ChandeMomentumOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ChandeMomentumOscillator': 1.0
        })
    )
