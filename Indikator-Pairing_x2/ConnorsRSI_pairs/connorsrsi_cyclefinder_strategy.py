import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'CycleFinder': 1.0
        })
    )
