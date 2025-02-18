import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'CycleFinder': 1.0
        })
    )
