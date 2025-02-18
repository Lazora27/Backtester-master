import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'LiquidityIndex': 1.0
        })
    )
