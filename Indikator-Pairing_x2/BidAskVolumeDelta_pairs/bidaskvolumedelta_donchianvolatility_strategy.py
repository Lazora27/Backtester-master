import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'DonchianVolatility': 1.0
        })
    )
