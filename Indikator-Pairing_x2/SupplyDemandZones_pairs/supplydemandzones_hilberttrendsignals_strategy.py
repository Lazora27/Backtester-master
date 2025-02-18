import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
