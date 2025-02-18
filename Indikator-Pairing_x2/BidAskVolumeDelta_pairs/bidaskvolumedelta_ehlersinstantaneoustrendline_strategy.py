import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
