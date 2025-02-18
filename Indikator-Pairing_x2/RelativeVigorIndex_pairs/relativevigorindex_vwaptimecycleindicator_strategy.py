import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_VWAPTimeCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und VWAPTimeCycleIndicator
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'VWAPTimeCycleIndicator': 1.0
        })
    )
