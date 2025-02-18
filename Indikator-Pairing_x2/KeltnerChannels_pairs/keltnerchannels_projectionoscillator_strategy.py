import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
