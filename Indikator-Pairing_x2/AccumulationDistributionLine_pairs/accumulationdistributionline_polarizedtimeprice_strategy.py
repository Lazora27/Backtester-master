import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
