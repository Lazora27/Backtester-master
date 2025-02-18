import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'FisherSignals': 1.0
        })
    )
