import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'WeeklyCycle': 1.0
        })
    )
