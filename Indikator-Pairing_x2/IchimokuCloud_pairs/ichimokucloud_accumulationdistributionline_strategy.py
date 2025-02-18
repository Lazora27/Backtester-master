import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
