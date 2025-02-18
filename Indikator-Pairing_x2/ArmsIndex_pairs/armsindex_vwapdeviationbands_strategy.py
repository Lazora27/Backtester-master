import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
