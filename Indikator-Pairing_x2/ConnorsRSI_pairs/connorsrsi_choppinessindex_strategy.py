import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
