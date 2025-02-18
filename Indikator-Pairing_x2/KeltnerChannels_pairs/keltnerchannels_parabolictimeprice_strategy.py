import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
