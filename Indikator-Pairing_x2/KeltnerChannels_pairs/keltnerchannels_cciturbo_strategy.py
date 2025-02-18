import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und CCITurbo
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'CCITurbo': 1.0
        })
    )
