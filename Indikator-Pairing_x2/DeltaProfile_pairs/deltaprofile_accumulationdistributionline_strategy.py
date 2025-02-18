import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
