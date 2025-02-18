import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'CycleFinder': 1.0
        })
    )
