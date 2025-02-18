import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
