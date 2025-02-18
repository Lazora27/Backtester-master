import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'SeasonalStrength': 1.0
        })
    )
