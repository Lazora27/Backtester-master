import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SmoothedCycle': 1.0
        })
    )
