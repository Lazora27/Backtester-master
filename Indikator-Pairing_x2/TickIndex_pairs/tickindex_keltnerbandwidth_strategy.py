import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
