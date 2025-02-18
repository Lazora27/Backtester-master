import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'CycleFinder': 1.0
        })
    )
