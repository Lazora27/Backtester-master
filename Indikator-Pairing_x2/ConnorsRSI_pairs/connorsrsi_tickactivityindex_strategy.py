import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TickActivityIndex': 1.0
        })
    )
