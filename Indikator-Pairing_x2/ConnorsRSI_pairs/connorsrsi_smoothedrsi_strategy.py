import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SmoothedRSI': 1.0
        })
    )
