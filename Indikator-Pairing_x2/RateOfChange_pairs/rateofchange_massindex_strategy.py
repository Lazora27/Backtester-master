import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MassIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MassIndex': 1.0
        })
    )
