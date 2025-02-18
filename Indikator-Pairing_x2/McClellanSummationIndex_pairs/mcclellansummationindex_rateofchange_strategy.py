import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
