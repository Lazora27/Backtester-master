import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'EhlersDecycler': 1.0
        })
    )
