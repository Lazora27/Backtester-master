import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'RateOfChange': 1.0
        })
    )
