import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'ProjectionBands': 1.0
        })
    )
