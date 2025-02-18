import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
