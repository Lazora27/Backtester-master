import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
