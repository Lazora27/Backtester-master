import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CVIRatio
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CVIRatio': 1.0
        })
    )
