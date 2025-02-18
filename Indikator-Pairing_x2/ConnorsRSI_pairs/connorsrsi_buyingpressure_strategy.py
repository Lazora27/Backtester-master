import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'BuyingPressure': 1.0
        })
    )
