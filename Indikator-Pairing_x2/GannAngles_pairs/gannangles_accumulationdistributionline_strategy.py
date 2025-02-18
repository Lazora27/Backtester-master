import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
