import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
