import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ConnorsRSI': 1.0
        })
    )
