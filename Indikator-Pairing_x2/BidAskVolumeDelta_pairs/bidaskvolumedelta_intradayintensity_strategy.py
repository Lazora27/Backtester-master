import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'IntradayIntensity': 1.0
        })
    )
