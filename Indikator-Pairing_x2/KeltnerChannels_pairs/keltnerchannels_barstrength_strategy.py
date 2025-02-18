import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und BarStrength
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'BarStrength': 1.0
        })
    )
