import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'BradleySiderograph': 1.0
        })
    )
