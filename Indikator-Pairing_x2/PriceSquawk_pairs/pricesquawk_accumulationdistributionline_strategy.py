import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
