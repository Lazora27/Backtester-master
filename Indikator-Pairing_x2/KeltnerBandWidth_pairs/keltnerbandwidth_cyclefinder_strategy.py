import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und CycleFinder
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'CycleFinder': 1.0
        })
    )
