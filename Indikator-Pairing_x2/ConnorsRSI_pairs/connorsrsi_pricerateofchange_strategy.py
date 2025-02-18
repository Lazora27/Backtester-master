import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
