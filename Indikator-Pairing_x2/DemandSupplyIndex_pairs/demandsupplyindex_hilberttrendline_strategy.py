import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
