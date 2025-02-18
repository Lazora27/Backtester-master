import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DemandIndex': 1.0
        })
    )
