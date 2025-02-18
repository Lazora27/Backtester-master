import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und COTReport
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'COTReport': 1.0
        })
    )
