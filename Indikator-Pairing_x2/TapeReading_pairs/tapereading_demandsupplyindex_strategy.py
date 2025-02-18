import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
