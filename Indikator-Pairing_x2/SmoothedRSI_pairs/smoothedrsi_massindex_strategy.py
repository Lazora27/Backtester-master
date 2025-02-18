import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MassIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MassIndex': 1.0
        })
    )
