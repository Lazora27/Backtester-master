import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ConnorsRSI': 1.0
        })
    )
