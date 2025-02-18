import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'LiquidityIndex': 1.0
        })
    )
