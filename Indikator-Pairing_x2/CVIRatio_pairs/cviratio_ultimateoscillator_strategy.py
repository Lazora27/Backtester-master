import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'UltimateOscillator': 1.0
        })
    )
