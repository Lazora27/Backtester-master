import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
