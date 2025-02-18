import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TimeCycle': 1.0
        })
    )
