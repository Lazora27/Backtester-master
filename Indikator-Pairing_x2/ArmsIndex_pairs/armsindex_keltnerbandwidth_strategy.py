import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
